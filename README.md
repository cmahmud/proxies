# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 480
- HTTP: 144 alive / 100 gold
- HTTPS: 110 alive / 42 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 205 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44929
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
