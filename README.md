# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 454
- HTTP: 135 alive / 85 gold
- HTTPS: 137 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46629
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
