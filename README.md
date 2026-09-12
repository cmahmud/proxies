# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 462
- HTTP: 128 alive / 95 gold
- HTTPS: 63 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49342
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
