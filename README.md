# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 361
- HTTP: 320 alive / 75 gold
- HTTPS: 232 alive / 11 gold
- SOCKS4: 229 alive / 125 gold
- SOCKS5: 231 alive / 150 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20279
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
