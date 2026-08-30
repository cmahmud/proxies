# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 419
- HTTP: 123 alive / 77 gold
- HTTPS: 68 alive / 30 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 191 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44061
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
