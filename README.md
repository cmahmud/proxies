# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 422
- HTTP: 307 alive / 93 gold
- HTTPS: 202 alive / 22 gold
- SOCKS4: 194 alive / 144 gold
- SOCKS5: 245 alive / 163 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28766
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
