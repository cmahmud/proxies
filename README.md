# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 412
- HTTP: 117 alive / 64 gold
- HTTPS: 167 alive / 17 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40994
- Ever gold: 1315

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
