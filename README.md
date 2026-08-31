# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 482
- HTTP: 135 alive / 103 gold
- HTTPS: 123 alive / 43 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45077
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
