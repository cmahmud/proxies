# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 464
- HTTP: 127 alive / 99 gold
- HTTPS: 59 alive / 33 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49334
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
