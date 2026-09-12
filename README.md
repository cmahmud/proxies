# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 464
- HTTP: 125 alive / 96 gold
- HTTPS: 55 alive / 33 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49409
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
