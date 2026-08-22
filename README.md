# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 406
- HTTP: 302 alive / 91 gold
- HTTPS: 197 alive / 21 gold
- SOCKS4: 199 alive / 130 gold
- SOCKS5: 271 alive / 164 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32149
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
