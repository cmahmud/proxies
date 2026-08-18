# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 237
- HTTP: 358 alive / 30 gold
- HTTPS: 163 alive / 8 gold
- SOCKS4: 242 alive / 113 gold
- SOCKS5: 204 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6828
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
