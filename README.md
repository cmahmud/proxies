# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 459
- HTTP: 136 alive / 87 gold
- HTTPS: 136 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46697
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
