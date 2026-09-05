# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 303
- HTTP: 258 alive / 77 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 191 alive / 68 gold
- SOCKS5: 187 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
