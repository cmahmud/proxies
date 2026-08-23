# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 307
- HTTP: 159 alive / 37 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 186 alive / 153 gold
- SOCKS5: 190 alive / 105 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32835
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
