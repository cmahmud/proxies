# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 344
- HTTP: 112 alive / 45 gold
- HTTPS: 83 alive / 11 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 183 alive / 135 gold

## Historical pool

- Discovered: 171032
- Ever alive: 32806
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
