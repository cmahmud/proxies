# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 418
- HTTP: 121 alive / 76 gold
- HTTPS: 69 alive / 30 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 192 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44063
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
