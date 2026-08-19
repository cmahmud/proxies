# SyndProxy private pool

## Current pool

- Alive now: 1355
- Gold now: 402
- HTTP: 460 alive / 91 gold
- HTTPS: 311 alive / 16 gold
- SOCKS4: 254 alive / 147 gold
- SOCKS5: 330 alive / 148 gold

## Historical pool

- Discovered: 133966
- Ever alive: 21672
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
