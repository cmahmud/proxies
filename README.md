# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 414
- HTTP: 109 alive / 65 gold
- HTTPS: 177 alive / 18 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40758
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
