# SyndProxy private pool

## Current pool

- Alive now: 1672
- Gold now: 622
- HTTP: 721 alive / 215 gold
- HTTPS: 547 alive / 143 gold
- SOCKS4: 170 alive / 104 gold
- SOCKS5: 234 alive / 160 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24726
- Ever gold: 1036

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
