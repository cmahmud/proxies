# SyndProxy private pool

## Current pool

- Alive now: 1616
- Gold now: 630
- HTTP: 683 alive / 248 gold
- HTTPS: 520 alive / 118 gold
- SOCKS4: 176 alive / 104 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24731
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
