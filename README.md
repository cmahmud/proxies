# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 453
- HTTP: 116 alive / 86 gold
- HTTPS: 111 alive / 34 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45651
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
