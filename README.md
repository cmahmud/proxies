# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 443
- HTTP: 128 alive / 80 gold
- HTTPS: 147 alive / 33 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44711
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
