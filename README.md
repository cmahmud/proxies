# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 429
- HTTP: 101 alive / 73 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48983
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
