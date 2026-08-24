# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 427
- HTTP: 144 alive / 77 gold
- HTTPS: 82 alive / 23 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33897
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
