# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 409
- HTTP: 350 alive / 95 gold
- HTTPS: 197 alive / 21 gold
- SOCKS4: 221 alive / 135 gold
- SOCKS5: 260 alive / 158 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32432
- Ever gold: 1181

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
