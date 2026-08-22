# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 437
- HTTP: 263 alive / 97 gold
- HTTPS: 176 alive / 33 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 258 alive / 163 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31049
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
