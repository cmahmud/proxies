# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 402
- HTTP: 93 alive / 61 gold
- HTTPS: 184 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40651
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
