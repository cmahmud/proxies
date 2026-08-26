# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 401
- HTTP: 144 alive / 80 gold
- HTTPS: 193 alive / 22 gold
- SOCKS4: 172 alive / 146 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39959
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
