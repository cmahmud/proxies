# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 424
- HTTP: 157 alive / 76 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 197 alive / 163 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33885
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
