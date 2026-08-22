# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 400
- HTTP: 255 alive / 93 gold
- HTTPS: 190 alive / 29 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 236 alive / 132 gold

## Historical pool

- Discovered: 161992
- Ever alive: 31303
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
