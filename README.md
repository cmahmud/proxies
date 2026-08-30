# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 420
- HTTP: 128 alive / 79 gold
- HTTPS: 76 alive / 30 gold
- SOCKS4: 157 alive / 151 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44069
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
