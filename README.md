# SyndProxy private pool

## Current pool

- Alive now: 1634
- Gold now: 619
- HTTP: 714 alive / 210 gold
- HTTPS: 520 alive / 143 gold
- SOCKS4: 171 alive / 104 gold
- SOCKS5: 229 alive / 162 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24717
- Ever gold: 1036

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
