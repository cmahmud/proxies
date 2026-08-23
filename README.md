# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 350
- HTTP: 127 alive / 40 gold
- HTTPS: 77 alive / 9 gold
- SOCKS4: 195 alive / 155 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32877
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
