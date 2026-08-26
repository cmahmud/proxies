# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 383
- HTTP: 131 alive / 72 gold
- HTTPS: 174 alive / 18 gold
- SOCKS4: 163 alive / 145 gold
- SOCKS5: 170 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39918
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
