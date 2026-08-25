# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 424
- HTTP: 109 alive / 67 gold
- HTTPS: 104 alive / 25 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35664
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
