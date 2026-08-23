# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 209
- HTTP: 130 alive / 34 gold
- HTTPS: 126 alive / 7 gold
- SOCKS4: 181 alive / 77 gold
- SOCKS5: 203 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
