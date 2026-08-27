# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 412
- HTTP: 97 alive / 63 gold
- HTTPS: 160 alive / 19 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40716
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
