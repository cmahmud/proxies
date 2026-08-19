# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 537
- HTTP: 409 alive / 161 gold
- HTTPS: 262 alive / 92 gold
- SOCKS4: 209 alive / 133 gold
- SOCKS5: 229 alive / 151 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18757
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
