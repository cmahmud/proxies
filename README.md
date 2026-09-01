# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 460
- HTTP: 144 alive / 91 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46664
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
