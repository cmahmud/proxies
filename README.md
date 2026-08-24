# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 424
- HTTP: 163 alive / 75 gold
- HTTPS: 89 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 205 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33869
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
