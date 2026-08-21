# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 390
- HTTP: 221 alive / 90 gold
- HTTPS: 104 alive / 22 gold
- SOCKS4: 187 alive / 122 gold
- SOCKS5: 230 alive / 156 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29461
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
