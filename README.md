# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 320
- HTTP: 317 alive / 49 gold
- HTTPS: 189 alive / 10 gold
- SOCKS4: 209 alive / 132 gold
- SOCKS5: 197 alive / 129 gold

## Historical pool

- Discovered: 128086
- Ever alive: 20031
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
