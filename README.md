# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 412
- HTTP: 106 alive / 68 gold
- HTTPS: 169 alive / 18 gold
- SOCKS4: 177 alive / 155 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40635
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
