# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 457
- HTTP: 128 alive / 85 gold
- HTTPS: 101 alive / 35 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 229 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45356
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
