# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 412
- HTTP: 137 alive / 71 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 189 alive / 159 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33708
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
