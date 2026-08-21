# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 399
- HTTP: 335 alive / 84 gold
- HTTPS: 186 alive / 27 gold
- SOCKS4: 232 alive / 142 gold
- SOCKS5: 230 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
