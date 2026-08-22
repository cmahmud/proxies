# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 413
- HTTP: 209 alive / 87 gold
- HTTPS: 153 alive / 29 gold
- SOCKS4: 191 alive / 143 gold
- SOCKS5: 238 alive / 154 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31850
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
