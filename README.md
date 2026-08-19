# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 399
- HTTP: 460 alive / 90 gold
- HTTPS: 299 alive / 16 gold
- SOCKS4: 254 alive / 146 gold
- SOCKS5: 328 alive / 147 gold

## Historical pool

- Discovered: 133965
- Ever alive: 21672
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
