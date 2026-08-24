# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 426
- HTTP: 152 alive / 77 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 195 alive / 164 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33894
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
