# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 414
- HTTP: 101 alive / 73 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33718
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
