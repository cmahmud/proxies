# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 406
- HTTP: 117 alive / 63 gold
- HTTPS: 54 alive / 15 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33676
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
