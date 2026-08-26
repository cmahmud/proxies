# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 380
- HTTP: 128 alive / 68 gold
- HTTPS: 181 alive / 17 gold
- SOCKS4: 157 alive / 145 gold
- SOCKS5: 175 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39876
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
