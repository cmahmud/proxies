# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 410
- HTTP: 97 alive / 63 gold
- HTTPS: 172 alive / 18 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40669
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
