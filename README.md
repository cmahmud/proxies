# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 445
- HTTP: 127 alive / 81 gold
- HTTPS: 157 alive / 33 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44709
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
